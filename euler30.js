var totalSum = 0;

// 199999 is the largest possible number
for ( var i = 199999; i >= 10; i-- ) {
  var sum = 0;
  var j = i;
  while ( j > 0 ) {
    sum += Math.pow(j % 10, 5);
    j = Math.floor(j / 10);
  }
  
  if ( sum == i )
    totalSum += sum;
}

console.log(totalSum);
