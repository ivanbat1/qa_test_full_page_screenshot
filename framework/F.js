window.scrollTo(0, document.body.scrollHeight);

function hide_header() {
    if (document.getElementsByTagName('header')) {
        document.getElementsByTagName('header')[0].style.display = 'none'
    } else {
        return null
    }
};
hide_header();