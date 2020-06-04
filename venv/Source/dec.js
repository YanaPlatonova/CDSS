const fs = require('fs');
const path = require('path');
const inputDir = `C:/CDSS/venv/Scripts/bolezni`
const outDir = `C:/CDSS/venv/Scripts/out`

fs.mkdirSync(outDir, { recursive: true });

const files = fs.readdirSync(inputDir);
for (const i in files) {
    const el = files[i];
    const inputPath = path.join(inputDir, el);
    const outPath = path.join(outDir, el);

    const contents = fs.readFileSync(inputPath, 'utf8');

    try {
        const tmp = JSON.parse(contents)
        const out = JSON.stringify(tmp, null, ' ')
        fs.writeFileSync(outPath, out);
    } catch (error) {
        console.log("skip", outPath);
        console.log(error);
        console.log("-------");
    }
}


// fs.readdir
// fs.readdir(inputDir, function (err, items) {
//     for (var i = 0; i < items.length; i++) {
//         const el = items[i];
//         console.log(el);

//         const outPath = path.join(outDir,el);

//         fs.writeFile(outPath, "Привет МИГ-29!")
//     }
// });