const fs = require('fs');
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
function walk(state) {
    let total = 0, small = 0;
    Object.keys(state).forEach(elm => {
        if (Number.isInteger(state[elm])) {
            total += state[elm];
        } else if (elm != "..") {
            res = walk(state[elm]);
            total += res.total;
            small += res.small;
        }
    });
    return {
        total: total,
        small: total <= 100000 ? small + total : small,
    } 
}
console.log(walk(state).small);
