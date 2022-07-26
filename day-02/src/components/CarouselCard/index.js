function CarouselCard(props) {
  let {name, image, index, handleClick} = props;

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

export default CarouselCard;
