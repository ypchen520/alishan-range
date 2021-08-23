var target = String("Start of Fall Semester");
const targetDate = '23 Aug 2021';

document.getElementById("header").innerHTML = target;

function countdown(){
    const tar = new Date(targetDate);
    const curr = new Date();
    const seconds = (tar - curr) * 1000;

    // const seconds

    console.log(tar - curr);
}

countdown();

setInterval(countdown, 1000);

