function palindrome(str) {
  let str2 = str.toLowerCase().replace(/\W/g,'').replace('_','');
  console.log(str2);
  let strbarr = []
  for (let i = 0; i < str2.length; i++){
    strbarr.unshift(str2[i]);
  }
  let strb = strbarr.join('')
  console.log(strb);
  if (str2 === strb){
    console.log(true);
    return true;
  }
  console.log(false);
  return false;
}
palindrome("race car");
