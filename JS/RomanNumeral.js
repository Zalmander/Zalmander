function convertToRoman(num) {
    let str1 = num.toString([10]);
    console.log(str1);
    let str = []
    for (let i=0; i<str1.length; i++){
        str.push(str1[i]);
    }
    console.log(str);
    while (str.length<4){
        str.unshift('0')
    }
    console.log(str[0]+str[1]);
    var thousands = 'M'.repeat(parseInt(str[0]));
    if (str[1]<4){
        var hundreds = 'C'.repeat(parseInt(str[1]));
    }
    else if (str[1]==4){
        var hundreds = 'CD';
    }
    else if (str[1]==5){
        var hundreds = 'D';
    }
    else if (str[1]>5&&str[1]<9){
        var hundreds = 'D' + 'C'.repeat(parseInt(str[1])-5);
    }
    else if (str[1]==9){
        var hundreds = 'CM';
    }
    else if (str[1]==0){
        var hundreds = '';
    }
    console.log(hundreds+1);
    if (str[2]<4){
        var tens = 'X'.repeat(parseInt(str[2]));
    }
    else if (str[2]==4){
        var tens = 'XL';
    }
    else if (str[2]==5){
        var tens = 'L';
    }
    else if (str[2]>5&&str[2]<9){
        var tens = 'L' + 'X'.repeat(parseInt(str[2])-5);
    }
    else if (str[2]==9){
        var tens = 'XC';
    }
    else if (str[2]==0){
        var tens = '';
    }    
    if (str[3]<4){
        var ones = 'I'.repeat(parseInt(str[3]));
    }
    else if (str[3]==4){
        var ones = 'IV';
    }
    else if (str[3]==5){
        var ones = 'V';
    }
    else if (str[3]>5&&str[3]<9){
        var ones = 'V' + 'I'.repeat(parseInt(str[3])-5);
    }
    else if (str[3]==9){
        var ones = 'IX';
    }
    else if (str[3]==0){
        var ones = '';
    }    
    console.log(thousands);
    console.log(hundreds);
    console.log(tens);
    console.log(ones);
    return(thousands+hundreds+tens+ones);
}
convertToRoman(16);
