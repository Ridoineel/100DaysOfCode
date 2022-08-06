import {Suspence} from "react"

function C(props) {
  let {name, image, index, handleClick} = props.props;

  return (
    <div
      class="card"
      index={index}
      style={{
        background: `url(${image})`,
        backgroundSize: "cover"
      }}
      onClick={handleClick}
    >
      <div>{name}</div>
    </div>
  )
}
function CarouselCard(props) {
  let {name, image, index, handleClick} = props;

  return (
    <Suspence >
      <C props={props} />
    </Suspence>
  )
}

export default CarouselCard;
