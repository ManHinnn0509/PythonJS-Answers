function log(s) {
    console.log(s);
}

function print(s) {
    process.stdout.write(s);
}

const readXlsxFile = require('read-excel-file/node');
const account = require("./account.js");        // Gmail Account for sending emails

// Files
const excelPath = "./customer.xlsx";
const mailFile1Path = "./mail-files/file-1.txt";
const mailFile2Path = "./mail-files/file-2.txt";

function logSkip(emailAddr, customerName, reason) {
    log("[SKIP] Skipping " + emailAddr + " (" + customerName + "). Reason: " + reason);
}

function sendMail(to, subject, text, files) {
    const send = require('gmail-send')({
        user: account.gmail,
        pass: account.passwd,
        to:   to,
        subject: subject,
        files: files        // Could be a single file path / array ???
    });

    send({
        // text: 'gmail-send example 1',  
	    text: text,
      }, (error, result, fullResult) => {
        if (error) {
            console.error(error);
            return false;
        } else {
            // log(result);
            // log(fullResult);        // JSON
            return true;
        }
    });
}

function isValidEmail(email) {
    // WTF is this regex
    // From https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const schema = {
    'name': {
        prop: 'name',
        type: String
    },
    'job': {
        prop: 'job',
        type: String
    },
    'age': {
        prop: 'age',
        type: Number
    },
    'email': {
        prop: 'email',
        type: String
    }
};

// File path.
readXlsxFile(excelPath, {schema}).then((rows) => {
    // log(rows);
    customers = rows['rows'];
    customers.forEach((customer) => {

        customerName = customer.name;
        to = customer.email;

        // Send to engineers only
        if (!(customer.job === "engineer")) {
            // continue;
            logSkip(to, customerName, "Job isn't engineer");
            return;
        }

        if (!isValidEmail(to)) {
            // continue;
            logSkip(to, customerName, "Invalid email address format.");
            return;
        }
        
        file = customer.age >= 30 ? mailFile1Path : mailFile2Path;
        print("[SEND] Sending email to " + to + " (" + customerName + ") with \"file-" + (customer.age >= 30 ? "1" : "2") + ".txt\"... ");
        result = sendMail(
            to, 
            "Dear " + customer.name + ", this is an email with attachment", 
            "Hello",
            file
        );

        print("[" + result ? "SUCCESS" : "FAILED" + "]");
        log("");        // New line since print doesn't support \n
    })
});