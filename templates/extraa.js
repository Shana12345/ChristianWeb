const ul = document.querySelector('.items');


ul.firstElementChild.innerHTML = '<br><strong> Canción de El Ánimo </strong><br><br>';
ul.children[1].innerHTML = '<strong> Dirección diaria </strong><br><br>';
ul.lastElementChild.innerHTML = '<strong> Motivación </strong>';

const btn = document.querySelector('.btn');
btn.style.background = 'red';
btn.style.color = 'yellow';