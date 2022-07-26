/*
* @params
*  pageContainer *
*  length (nb pages) *
*  pageRatio *
*  initPage (initial page index)
*  ...
*/
function CarouselPagination(props) {
    let {pagesContainer, length, pageRatio, setInitCard} = props;
    let initPage = props.init || 0;
    let pageWidth;
    let buttons = []

    for (let i=0; i < length; i++) {
        buttons.push(
            (i == initPage) ?
            <span onClick={carPagHandleClick} key={i} num={i} className="active"></span>
                :
            <span onClick={carPagHandleClick} key={i} num={i}></span>
        )
    }

    function carPagHandleClick(event) {

        let btn = event.target;
        let btns = document.querySelectorAll(".carousel-pagination span");
        let curPressedBtnPage = btn.getAttribute("num");

        pageWidth = pagesContainer.current.offsetWidth * pageRatio

        // distance beetwen start page
        // and initial page
        let dist;

        // activate this btn
        btn.classList.add("active");

        // deactivete btns if != target btn
        btns.forEach((item, i) => {
            (item != btn) &&  item.classList.remove("active")
        });

        // move pages container
        dist = curPressedBtnPage*pageWidth - pageWidth/2
        pagesContainer.current.style.transform = `translateX(${-dist}px)`

        // update initial card
        setInitCard(curPressedBtnPage)
    }

    return (
        <div class="carousel-pagination">
            {buttons.map((btn, i) => {
                return btn
            })}
        </div>
    )
}

export default CarouselPagination;
