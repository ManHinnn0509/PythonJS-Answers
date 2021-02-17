function log(s) {
    console.log(s);
}

function print(s) {
    process.stdout.write(s);
}

function decimalPlace(num, dec) {
    const n = Math.pow(10, dec);
    return Math.round(num * n) / n;
}

const ffmpegPath = "C:/ffmpeg/ffmpeg.exe";
const outputPath = "./";

var scanf = require('scanf');
var YoutubeMp3Downloader = require("youtube-mp3-downloader");

// Configure YoutubeMp3Downloader with your settings
var YD = new YoutubeMp3Downloader({
    "ffmpegPath": ffmpegPath,       // FFmpeg binary location
    "outputPath": outputPath,                     // Output file location (default: the home directory)
    "youtubeVideoQuality": "highestaudio",      // Desired video quality (default: highestaudio)
    "queueParallelism": 2,                      // Download parallelism (default: 1)
    "progressTimeout": 3 * 1000,                // Interval in ms for the progress reports (default: 1000)
    "allowWebm": false                          // Enable download from WebM sources (default: false)
});

print("Input video ID here: ");
var videoID = scanf("%s");

//Download video and save as MP3 file
YD.download(videoID);

YD.on("progress", function(progress) {
    // progress is a JSONObject
    log("Downloading... [PROGRESS] " + decimalPlace(progress.progress.percentage, 1) + " %");

    /*
    progress:

{
    "videoId":"scmvAg_S97k",
    "progress":{
        "percentage":55.67016157136202,
        "transferred":1982464,
        "length":3561089,
        "remaining":1578625,
        "eta":2,
        "runtime":2,
        "delta":1982464,
        "speed":792985.6
    }
}
    */
});

YD.on("finished", function(err, data) {
    // log(JSON.stringify(data));
    log("Download done! MP3 file directory: \"" + outputPath + "\" " + (outputPath === "./" ? "(Current directory)" : ""));

    /*
    data:

{
    "videoId":"scmvAg_S97k",
    "stats":{
        "transferredBytes":3561089,
        "runtime":3,
        "averageSpeed":890272.25
    },
    "file":"./HW-2/My Michelle.mp3",
    "youtubeUrl":"http://www.youtube.com/watch?v=scmvAg_S97k",
    "videoTitle":"My Michelle",
    "artist":"Unknown",
    "title":"My Michelle",
    "thumbnail":"https://i.ytimg.com/vi/scmvAg_S97k/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLDliouYoEyAY__1yaswrOwiRIb1Pw"
}

    */
});

YD.on("error", function(error) {
    log("Something went wrong");
    log(error);
});