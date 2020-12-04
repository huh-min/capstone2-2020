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
        상세보기
      </b-button>
      <slot name="additionalButton"></slot>
    </template>
  </b-overlay>
</template>

<script>
import axios from 'axios'
import consts from '@/consts.js'
export default {
  data: function () {
    return {
      categoryData: '',
      noCategorydataMessage: '',
      showCategoryAlert: false,
      alertMessage: '',
      showAlert: false,
      isHovered: false
    }
  },
  props: [
    'clothes',
    'categorydata'
  ],
  methods: {
    handleClick: function () {
      this.$router.push({ name: 'ClosetDetail', params: { clothes_id: this.clothes.id, clothes_category: this.clothes.category } })
    },
    handleHover: function (hovered) {
      this.isHovered = hovered
    }
  },
  created: function () {
    if (!localStorage.getItem('token')) {
      this.$router.push({
        name: 'Bridge',
        params: {
          errorMessage: '로그인이 필요한 서비스입니다.',
          destination: 'login',
          delay: 3,
          variant: 'danger'
        }
      })
    } else {
      var token = window.localStorage.getItem('token')
      var config = {
        headers: { Authorization: `Bearer ${token}` }
      }
      var categoryId = this.clothes.category
      if (categoryId === undefined) {
        categoryId = this.clothes.category_id
      }
      axios.get(`${consts.SERVER_BASE_URL}/categorydata/category/?category_id=${categoryId}`, config)
        .then((response) => {
          this.categoryData = response.data
          if (this.categoryData.length === 0) {
            this.noCategorydataMessage = '등록된 옷이 없습니다. 옷을 등록해 주세요'
            this.showCategoryAlert = true
          }
        }).catch((ex) => {
          this.alertMessage = '옷을 불러올 수 없습니다. 다시 시도해주세요'
          this.showAlert = true
        })
    }
  }
}
</script>

<style>

</style>
