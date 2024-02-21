const fs = require('fs');
/*fs.readFile('test.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
*/

const content = "Happened yesterday!"

fs.appendFile('test.txt', content, err => {
  if (err) {
    console.error(err)
  }
});