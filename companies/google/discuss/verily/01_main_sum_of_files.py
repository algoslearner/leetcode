# https://leetcode.com/discuss/interview-question/682399/Verily-SE-phone-interview-rejected
'''
You have a bunch of files (N files in particular)
Each file has a bunch of numbers in it
You have a bunch of machines(as many as you want)
Goal: Find the sum of all the numbers in all the files (n1 + n2 + n3) + (n4+n5+n6) ..... = TotalSumAnswer
total(fileId: number, machineId: number): sums up all the numbers in the file corresponding to fieldId,
by spawning a job to run to do that work on the machine identified by machineId. when the job finishes it returns that sum.

Write a program that utilizes total() in order to find the main sum of all the files.
'''

# My Solution:

let filesMap = {};
let machinesMap = {};

//For generating files & numbers:
function generateFiles(N) {
  return new Promise((resolve, reject) => {
    if(N>0) {
      for(let i = 1; i <= N; i++) {
        filesMap['f'+[i]] = [i, i+1, i+2]
      }
      resolve(filesMap);
    } else {
      reject("File length should be greater than 0")
    }
  })
}
//generating two files
generateFiles(2).then((res) => {
  let j = 1;
  for(let i in res) {
    total(i, 'm'+ j);
    j++;
  }
});
//adding files based on fieldId, and mapping to machine id
function total(fileid, machineid) {
    machineWork(filesMap[fileid], machineid);
}

function machineWork(numsArr, machineId) {
    let sum = 0;
    numsArr.forEach((val, i) => {
        sum += val;
    })
    machinesMap[machineId] = sum;
    sumAllFiles(machinesMap)
}
//total sum of file numbers
function sumAllFiles(machinesMap) {
    let sum = 0;
    for(let i in machinesMap) {
        sum += machinesMap[i];
    }
    console.log(sum);
}
