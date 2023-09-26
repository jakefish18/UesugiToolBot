<script>
export default {
  data() {
    return {
      name: "name",
      author: "author",
      downloads_count: 1,
      rating: 1
    };
  },
}
</script>

<template>
  <div class="search-result">
    <label>Автор: {{ author }}</label>
    <label>Название: {{ name }}</label>
    <label>Количество скачиваний: {{ downloads_count }}</label>
    <label>Средняя оценка: {{ rating }}</label>
  </div>
</template>

<style scoped>

.search-result {
  display: flex;
  flex-direction: column;
  color: white;
}


</style>