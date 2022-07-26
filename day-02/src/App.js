import {useRef, useState, useEffect} from "react"
import CarouselCard from "./components/CarouselCard"
import CarouselPagination from "./components/CarouselPagination"
import MyGithubButton from "./components/MyGithubButton"

import Img1 from "./assets/images/img1.jpg"
import Img2 from "./assets/images/img2.jpg"
import Img3 from "./assets/images/img3.jpg"
import Img4 from "./assets/images/img4.jpg"
import Img5 from "./assets/images/img5.jpg"
import Img6 from "./assets/images/img6.jpg"
import Img7 from "./assets/images/img7.jpg"
import Img8 from "./assets/images/img8.jpg"
import Img9 from "./assets/images/img9.jpg"
import Img10 from "./assets/images/img10.jpg"

let cards = [

  {
    name: "SORA & ERINA - FOOD WARS",
    image: Img1
  },
  {
    name: "TELESCOPE VIEW - SPACE",
    image: Img2
  },
  {
    name: "SORA & ERINA - FOOD WARS",
    image: Img3
  },
  {
    name: "EREN - ATTACK ON TITAN",
    image: Img4
  },
  {
    name: "SORA - FOOD WARS",
    image: Img5
  },
  {
    name: "LIVAÏ & EREN - ATTACK ON TITAN",
    image: Img6
  },
  {
    name: "ALGORITHM - CODING",
    image: Img7
  },
  {
    name: "HACKER - HACKING",
    image: Img8
  },
  {
    name: "MATHEMATIC - SCIENCE",
    image: Img9
  },
  {
    name: "THACKER - HACKING",
    image: Img10
  },
]

function App() {
  let cardsContainer = useRef(0);
  let [initCard, setInitCard] = useState(2)

  function cardHandleClick(e) {
    let card = e.target;
    let cardIndex = Number(card.getAttribute("index"));

    if (cardIndex != initCard) {
      let paginationButton = document.querySelectorAll(".carousel-pagination span")[cardIndex];

      paginationButton.click();
    }

  }

  useEffect(() => {
    // activate current card
    // deactivate the others
    for (let i=0; i<cardsContainer.current.children.length; i++) {
      let item = cardsContainer.current.children[i];

      if (i==initCard)
        item.classList.add("active");
      else
        item.classList.remove("active");
    }

    // change background
    let img = cards[initCard].image;
    let carouselBgPanel = document.querySelector(".carousel__background-panel")

    carouselBgPanel.style.backgroundImage = `url(${img})`;
    carouselBgPanel.style.backgroundSize= "cover";
  }, [initCard])

  return (
    <div className="App">
      <div class="carousel__background-panel">
      </div>

      <div class="carousel__cards">
        <div class="container" ref={cardsContainer}>
          {cards.map((item, i) => {
            return <CarouselCard
                      key={i}
                      index={i}
                      handleClick={cardHandleClick}
                      name={item.name}
                      image={item.image}
                   />
          })}
        </div>

        <CarouselPagination
          init={initCard}
          setInitCard={setInitCard}
          length={cards.length}
          pagesContainer={cardsContainer}
          pageRatio="0.5"
        />
      </div>

      <MyGithubButton />
    </div>
  );
}

export default App;
