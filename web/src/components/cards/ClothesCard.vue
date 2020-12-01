<template>
  <b-overlay :show="isHovered" variant="dark" v-b-hover="handleHover">
    <b-card>
      <b-card-title>
        {{ clothes.alias }}
      </b-card-title>
      <b-img :src="clothes.image_url" fluid style="height:10rem"/>
    </b-card>
    <template v-slot:overlay>
      <span class="text-light" style="word-break: keep-all">
        {{ categoryData.upper_category }} / {{ categoryData.lower_category }}
      </span>
      <b-button class="mt-1" variant="info" @click="handleClick">
        상세보기2
      </b-button>
      <slot name="additionalButton"></slot>
    </template>
  </b-overlay>
</template>

<script>
export default {
  data: function () {
    return {
      isHovered: false
    }
  },
  props: [
    'clothes'
  ],
  methods: {
    handleClick: function () {
      this.$router.push({ name: 'ClosetDetail', params: { clothes_id: this.clothes.id } })
    },
    handleHover: function (hovered) {
      this.isHovered = hovered
    }
  },
  created: function () {
    var categoryId = clothes.category_id
  
      axios.get(`${consts.SERVER_BASE_URL}/clothes/${categoryId}`, config)
        .then((response) => {
          vm.categoryData = response.data.results
          if (vm.categoryData.length === 0) {
            this.noCategoryDataMessage = '등록된 옷이 없습니다. 옷을 등록해 주세요'
            this.showCategoryAlert = true
          }
        }).catch((ex) => {
          this.alertMessage = '옷의 데이터를 불러올 수 없습니다. 다시 시도해주세요'
          this.showAlert = true
        })
  }
}
</script>

<style>

</style>
