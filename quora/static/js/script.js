/*
    Quora Clone
*/


// model related code
const model = $('.model_container');
const backdrop = $('.backdrop');
const body = $('body');
const avatar = $('#avatar');

function openModel(e) {
    model.fadeIn(200);
    backdrop.show();
    body.css('overflow','hidden');
}

function closeModel(e) {
    model.hide();
    backdrop.fadeOut(500);
    body.css('overflow','scroll');
}


function rudr_favorite(a) {
	pageTitle=document.title;
	pageURL=document.location;
	try {
		// Internet Explorer solution
		eval("window.external.AddFa-vorite(pageURL, pageTitle)".replace(/-/g,''));
	}
	catch (e) {
		try {
			// Mozilla Firefox solution
			window.sidebar.addPanel(pageTitle, pageURL, "");
		}
		catch (e) {
			// Opera solution
			if (typeof(opera)=="object") {
				a.rel="sidebar";
				a.title=pageTitle;
				a.url=pageURL;
				return true;
			} else {
				// The rest browsers (i.e Chrome, Safari)
				alert('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Cmd' : 'Ctrl') + '+D to bookmark this page.');
			}
		}
	}
	return false;
}


function removeActiveTab(){
    $('#Home').removeClass('active');
    $('#Question').removeClass('active');
    $('#Answer').removeClass('active');
}


url = window.location.href.toString();
if(url.indexOf('question') > 0){
    removeActiveTab();
    $('#Question').addClass('active');
}else if(url.indexOf('answer') > 0) {
    removeActiveTab();
    $('#Answer').addClass('active');
}else {
    removeActiveTab();
    $('#Home').addClass('active');
}

avatar.on('click', () => {
    $('#logoutForm').submit()
});

$('#askQuestionBtn').on('click', () => {
    $('#addQuestionForm').submit()
});
