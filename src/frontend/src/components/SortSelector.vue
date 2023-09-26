<script>
export default {
}
</script>

<template>
  <div class="sort-radio">
    Сортировать по:
    <div class="sort-radio-item">
      <input type="radio" id="popularity" name="sort-type" value="popularity">
      <label for="popularity">по популярности</label><br>
    </div>
    <div class="sort-radio-item">
      <input type="radio" id="downloads-count" name="sort-type" value="downloads-count">
      <label for="css">по количеству скачиваний</label><br>
    </div>
  </div>
</template>

<style scoped>

.sort-radio{
  display: flex;
  color: white;
}


</style>