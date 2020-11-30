<template>
<b-container>
    <b-alert id="Alert" v-model="showAlert" variant="success" dismissible style="word-break: keep-all">
    {{ alertMessage }}
    </b-alert>
    <b-row>
        <b-col cols="4" class="text-left">
            <b-button to="/cody">뒤로가기</b-button>
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
            <b-row>
                <ReviewAnalysisComponent :analysis_props.sync="analysis_props" :isDisabled="disableAnalysis" />
            </b-row>
            <b-row>
                <b-col cols="6">
                  <b-button pill class="w-75 button" @click="handleModify">수정하기</b-button>
                </b-col>
                <b-col cols="6">
                  <b-button pill class="w-75 button" @click="handleUpdate">확인하기</b-button>
                </b-col>
              </b-row>
        </b-col>
    </b-row>
</b-container>
</template>

<script>
import consts from '@/consts.js'
import axios from 'axios'
import ReviewAnalysisComponent from '@/components/ReviewAnalysisComponent.vue'
export default {
  components: {
    ReviewAnalysisComponent
  },
  data: function () {
    return {
      showAlert: false,
      alertMessage: '',
      analysis_props: {
        comment: '',
        review: '3'
      },
      disableAnalysis: true
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
  },
  methods: {
    handleModify: function () {
      this.disableAnalysis = false
    },
    handleUpdate: function () {
      var vm = this
      var reviewId = vm.review.id
      var token = window.localStorage.getItem('token')
      var config = {
        headers: { Authorization: `Bearer ${token}` }
      }
      var data = {
        comment: vm.analysis_props.comment,
        review: vm.analysis_props.review
      }
      axios.patch(`${consts.SERVER_BASE_URL}/clothes-set-reviews/${reviewId}/`, data, config)
        .then(response => {
          this.alertMessage = '옷의 리뷰를 수정했습니다.'
          this.showAlert = true
          vm.analysis_props.comment = response.data.comment
          vm.analysis_props.review = response.data.review
          vm.disableAnalysis = true
        }).catch((ex) => {
          this.alertMessage = '해당 옷의 리뷰를 수정할 수 없습니다. 다시 시도해주세요'
          this.showAlert = true
          console.log(ex)
        })
    }
  }
}
</script>

<style scoped>
h3 {
    padding-top: 30px;
    padding-bottom: 20px;
}
.button {
    margin-top: 30px;
}
</style>
