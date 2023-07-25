document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // event to send a mail
  document.querySelector('#btn-send-mail').addEventListener('click', send_mail);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // use API to get emails
  fetch(`emails/${mailbox}`)
  .then(response =>	response.json() )
  .then(emails => {
	console.log(emails);
	emails.forEach(list_mail);
  })
}

// print list of mails on <mailbox>
function list_mail(mail){
	const element = document.createElement('div');
	element.className = `list-mail card row mb-3`;
	element.id = mail.id;
	element.dataset.mail = mail.id;
	element.innerHTML = `<h3 class='card-title col-md-4'>${mail.sender}</h3> 
						<p class='card-text col-md-4'>${mail.subject}</p>
						<div class='text-muted col-md-4'>${mail.timestamp}</div>`;
	document.querySelector('#emails-view').append(element);

	element.addEventListener('click', read_mail);
}

// send mail with data packaged in JSON
function send_mail(){
	// create object to send
	mail = {
		subject: document.querySelector('#compose-subject').value,
		body: document.querySelector('#compose-body').value,
		recipients: document.querySelector('#compose-recipients').value
	}

	// send JSON to server 
	fetch('/emails', {
		method: 'POST',
		body: JSON.stringify(mail)
	})
	.then(response => response.json())
	.then(result => {
	    // Print result
	    console.log(result);
	});
	load_mailbox('sent');
}

function read_mail(element) {
	let id;

	// get mail id from the clicked element
	if (element.target.dataset.mail == undefined){
		// console.log(element.target.parentElement.dataset.mail);
		id = element.target.parentElement.dataset.mail;
	} else {
		// console.log(element.target.dataset.mail);
		id = element.target.dataset.mail;
	}

	fetch(`emails/${id}`)
  	.then(response =>	response.json() )
  	.then(email => {
		let mail = document.createElement('div').innerHTML = `<h5><b>From: </b>${email.sender}</h5>
			<h5><b>To: </b>${email.recipients}</h5>
			<h5><b>Subject: </b>${email.subject}</h5>
			<h5><b>TimeStamp: </b>${email.timestamp}</h5>
			<button class="btn btn-sm btn-outline-primary" id="reply" >Reply</button>
			<button class="btn btn-sm btn-outline-primary" id="archive" >Archive</button>
			<hr>
			<br>
			<p>${email.body}</p>`;
		
		document.querySelector('#emails-view').innerHTML = mail;
  	})

}