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
  name: 'reviewmodifycomponent',
  data: function () {
    return {
      showAlert: false,
      alertMessage: ''
    }
  },
  props: [
    'review'
  ]
}
</script>

<style scoped>
h3{
    padding-top: 30px;
    padding-bottom: 20px;
}
</style>
