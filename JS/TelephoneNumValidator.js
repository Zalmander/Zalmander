function telephoneCheck(str) {
  if (str.indexOf('?')!=-1 || str.indexOf('-')==0){
    return false;
  }
  if (isFinite(str[str.length-1])!==true){
    console.log('not a number');
    return false;
  }
  var bad = []
  for (let i = 0; i < str.length; i++){
    if (isNaN(str[i])){
      bad.push(str[i]);
    }
  }
  if ((bad.indexOf('(')==-1 && bad.indexOf(')')!=-1) || (bad.indexOf(')')==-1 && bad.indexOf('(')!=-1))
    {
    console.log('one parentheses')
    return false;
  }
  console.log(bad);
  let array = str.split(/\W|\(|\)/);
  let str1 = array.join('');
  var array1 = str1.split('')
  if (array1.length>11){
    return false;
  }
  while (array1.length<11){
    array1.unshift('A');
  }
  console.log(array1);
  if ((array1[0]!=1)&&array1[0]!='A'){
    console.log(array1[0]);
    return false;
  }
  if (isNaN(array1[1])==true){
    console.log('notenoughnumbers');
    return false;
  }
  return true;
}

telephoneCheck("1 456 789 4444");
