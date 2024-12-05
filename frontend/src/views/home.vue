<template>
  <div class="gallery-container">
    <div class="gallery-wrapper">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/03f63f5fe13b4cb994f7f82af912ed64800f4fba07839ebe49c033b475648fea?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-background"
        alt=""
      />
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/746a97cb32fcc0e663949dd8a4e00662dd6fb2957f4ffb8fcbbd6411133003e9?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-header"
        alt="Gallery Header"
      />
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/d58f3000989a01d360aa6b718bf2a1da619b65250a41c5c91f8d6192282d4246?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-content"
        alt="Gallery Content"
      />
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/4a8febd21bfe1feaeaa099720a3e2ffe159c07ff180a36ffd7064a04500b571c?placeholderIfAbsent=true&apiKey=b0ba032ba04c496389e8dea963537aea"
        class="gallery-footer"
        alt="Gallery Footer"
      />
    </div>
  </div>
</template>

<style scoped>
.gallery-container {
  background-color: blue;
  display: flex;
  max-width: 480px;
  width: 100%;
  flex-direction: column;
  overflow: hidden;
  margin: 0 auto;
}

.gallery-wrapper {
  display: flex;
  flex-direction: column;
  position: relative;
  aspect-ratio: 0.461;
  width: 100%;
  padding: 106px 0;
}

.gallery-background {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
}

.gallery-header {
  aspect-ratio: 1.22;
  object-fit: contain;
  object-position: center;
  width: 219px;
  max-width: 100%;
}

.gallery-content {
  aspect-ratio: 1.26;
  object-fit: contain;
  object-position: center;
  width: 100%;
  margin-top: 89px;
}

.gallery-footer {
  aspect-ratio: 3.45;
  object-fit: contain;
  object-position: center;
  width: 207px;
  align-self: center;
  max-width: 100%;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>