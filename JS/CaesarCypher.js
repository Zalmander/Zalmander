function rot13(str) {
  let decoder = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
  var darr = [];
  for (let i = 0; i<str.length; i++){
    if (decoder.indexOf(str[i])==-1){
      darr.push(str[i]);
    }
    else {
      darr.push(decoder[decoder.indexOf(str[i])+13])
    }
  }
  console.log(darr);
  let final = darr.join('');
  console.log(final);
  return final;
}

rot13("SERR PBQR PNZC");


