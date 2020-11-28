<template>
<b-container>
    <b-alert id="Alert" v-model="showAlert" variant="danger" dismissible style="word-break: keep-all">
    {{ alertMessage }}
    </b-alert>
    <b-row>
        <b-col cols="4" class="text-left">
            <b-button to="/cody/detail">뒤로가기</b-button>
        </b-col>
    </b-row>
    <b-row>
        <b-col cols="12">
            <h3 class="text-center text-top">리뷰   수정</h3>
        </b-col>
    </b-row>
    <b-row>
        <b-col md="6" cols="12">
            <b-img :src="review.clothes_set.image_url" fluid style="height:30rem"/>
        </b-col>
        <b-col md="6" cols="12">
        </b-col>
    </b-row>
</b-container>
</template>

<script>
import consts from '@/consts.js'
import axios from 'axios'

export default {
  data: function () {
    return {
      showAlert: false,
      alertMessage: ''
    }
  },
  props: [
    'review'
  ],
  created: function () {
    var vm = this
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
      if (vm.review.id === undefined) {
        this.$router.push({
          name: 'Bridge',
          params: {
            errorMessage: '해당 리뷰가 없습니다.',
            destination: 'Cody',
            delay: 3,
            variant: 'danger'
          }
        })
      } else {
        var token = window.localStorage.getItem('token')
        var config = {
          headers: { Authorization: `Bearer ${token}` }
        }
        var url = consts.SERVER_BASE_URL + '/clothes-set-reviews/'
        url += this.review.id + '/'
        axios.get(url, config)
          .then(response => {
            console.log(response)
          }).catch((ex) => {
            this.alertMessage = '코디 리뷰를 불러오지 못하였습니다. 오류가 계속 될 경우, 관리자에게 연락해주세요.'
            this.showAlert = true
          })
      }
    }
  }
}
</script>

<style scoped>
h3{
    padding-top: 30px;
    padding-bottom: 20px;
}
</style>
