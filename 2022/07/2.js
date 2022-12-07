const fs = require('fs');
const FS_SIZE = 70000000;
const NEED_FS = 30000000;
const data = fs.readFileSync('input', 'utf8');
// This savage oneliner will change input to array of tokenised commands.
const commands = data.split("$").slice(2).map(x => x.split(/[ \n]/).slice(1, -1));
// That's actually quite nice.
let state = commands.reduce((state, cmd) => {
    if (cmd[0] == "ls") {
        for (let i = 1; i < cmd.length; i += 2) {
            state[cmd[i+1]] = (cmd[i] == "dir") ? {"..": state} : parseInt(cmd[i]);
        }
    } else { state = state[cmd[1]]; }
    return state;
},{});
// Go back to the root (ugly, imperative).
while (".." in state) { state = state[".."]; }
// Recursively walk and sum the directories (ugly but good enough).
function walk(state, free) {
    let total = 0, best = FS_SIZE;
    Object.keys(state).forEach(elm => {
        if (Number.isInteger(state[elm])) {
            total += state[elm];
        } else if (elm != "..") {
            res = walk(state[elm], free);
            total += res.total;
            best = Math.min(res.best, best);
        }
    });
    return {
        total: total,
        best: free + total >= NEED_FS ? Math.min(best, total) : best,
    }
}
const diskuse = walk(state, 0).total;
console.log(walk(state, FS_SIZE - diskuse).best);
