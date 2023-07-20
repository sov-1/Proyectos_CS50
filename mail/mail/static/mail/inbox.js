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
	element.className = 'list-mail card';
	element.innerHTML = `<h3 class='card-title'>${mail.sender}</h3> 
						<p class='card-text'>${mail.subject}</p>
						<p class='card-text timestamp'>${mail.timestamp}</p>`;
	document.querySelector('#emails-view').append(element);
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