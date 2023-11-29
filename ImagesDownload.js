let images = document.querySelectorAll('img');

for (let i of images){
    let a = document.createElement('a');
    a.href = i.src;
    console.log(i);
    a.download = i.src;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}