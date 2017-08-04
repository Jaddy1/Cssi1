function timesTwo(number){
  var value = number * 2
  return value
}

function timesSix(number){
  var result = timesTwo(number)*3;
  return result
}

function rollDice(){
  return Math.floor((Math.random()*6)+1);
}
function finalCost(bill,tax,tip){
  var modifiedAmnt = bill + bill*tax;
  return modifiedAmnt + tip;
}


function scoreChecker(score){
  if(score > 450){
    window.alert("Your score is beasty")
  }else if(score < 450 && score >= 350){
    window.alert("You're donig great")
  }else if(score < 350 && score >= 250){
    window.alert("Your score is pretty good")
  }else if(score < 250 && score >= 150){
    window.alert("Your score is decent")
  }else{
    window.alert("Get better")
  };
}

var groceries = ['apple', 'banana', 'orange', 'pineapple']
function groceryReverse(){
  groceries.pop('apple');
  groceries.pop('banana');
  groceries.pop('orange');
  groceries.pop('pineapple');
  groceries.push('pineapple');
  groceries.push('orange');
  groceries.push('banana');
  groceries.push('apple');
  return groceries
}

// function arrayDouble(originalArray){
//   var originalArray = [1, 2, 3, 4];
//   for(var i=0; i < originalArray.length; i++){
//     var number = originalArray[i]*2;
//     alert(number);
//   }
// }

// function reversedArray(originalArray){
//   var originalArray = [1, 2, 3, 4, 5, 6]
//   var length = originalArray.length
//   var newArray = [];
//   var letters = ['a', 'b', 'c', 'd', 'e'];
//   for(var i=0; i < length; i++){
//     newArray.push(originalArray.pop(i));
//     newArray.push(letters.pop(i));
//   }
//   return newArray
// }
function lettersAndNumbers(numbers){
  var numbers = [1, 2, 3];
  var letters = ['a', 'b', 'c', 'd', 'e']
  var length = Math.max(letters.length, numbers.length);
  var newArray = [];
  for(var i=0; i<length; i++){
    // newArray.push(numbers[i])
    // newArray.push(letters[i])
    if(numbers[i] != undefined){
      newArray.push(numbers[i]);
    }if(letters[i] != undefined){
      newArray.push(letters[i]);
    }
  }
  console.log(newArray)
}


var johnLennonFacts = ["He was the guitarist in the Beatles", "He Had a son named Julian", "He is cool"]
var excitingFacts = []
function johnLennonFactsFunc() {
  x=0
  while(x<3){
    excitingFacts.push(johnLennonFacts[x] + "!!!");
    //return excitingFacts;
    x++;
  }
  return excitingFacts;
}

var musicians = ["John Lennon", "Paul McCarthy", "George Harrison", "Ringo Starr", "Pete Best", "Stuart Sutcliffe"];
var musicianRoles = [];
var instruments = ["plays the Guitar", "plays the Bass", "plays the Lead Guitar", "plays the Drums", "plays the Drums", "plays the Bass"];
function beatlesMusicians(){
  for( var i = 0; i < musicians.length; i++){
    musicianRoles.push(musicians[i] + " " + instruments[i]);
  }
  return musicianRoles
}
