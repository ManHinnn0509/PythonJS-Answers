// Util
function log(s) {
    console.log(s);
}

function randDouble() {
    return Math.random();
}

// 1
let candidate = ["柯文哲","丁守中","姚文智"];
candidate.push("XXX");

log("現在參選人有" + candidate.length + "位，請他們發言：）");
candidate.forEach((c) => {
    log("你好，我是" + c + "，請投給我！");
});


// 2
function lottery() {
    n = randDouble();
    
    s = "沒中獎";
    if (n < 0.2) {
        s = "中獎";
    }

    // log("Num = " + n + ", s = " + s);
    return [n, s];
}

log("");
r = lottery();
log("Num = " + r[0] + ", s = " + r[1]);

// 3-2
log("\n3-2 [for迴圈連續開三次]");
for (x = 0; x < 3; x++) {
    result = lottery();
    log("Num = " + result[0] + ", s = " + result[1]);
}

// 3-1
log("\n3-1 [利用setInterval，每5秒開一次獎。]");
setInterval(function() {
    result = lottery();
    log("Num = " + result[0] + ", s = " + result[1] + " [" + new Date() + "]");
}, 5 * 1000);