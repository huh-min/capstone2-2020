<template>
    <b-container>
      <b-alert id="alert" v-model="showAlert" variant="success" dismissible >
        {{ alertMessage }}
      </b-alert>
        <b-row>
          <b-col md="6" cols="12" style="text-align:left">
            <b-button to="/closet">뒤로가기</b-button>
          </b-col>
          <b-col md="6" cols="12" style="text-align:right">
            <b-button @click="deleteClothe">삭제하기</b-button>
          </b-col>
        </b-row>
        <b-row>
            <b-col md="6" cols="12">
              <b-img fluid :src="clothes.image_url"/>
            </b-col>
            <b-col md="6" cols="12">
              <b-row>
                <ImageAnalysisComponent :analysis_props.sync="analysis_props" :isDisabled="disableAnalysis" />
              </b-row>
              <b-row>
                <b-col cols="6">
                  <b-button pill class="w-75" @click="handleModify">수정하기</b-button>
                </b-col>
                <b-col cols="6">
                  <b-button pill class="w-75" @click="handleUpdate">확인하기</b-button>
                </b-col>
              </b-row>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import axios from 'axios'
import consts from '@/consts.js'
import ImageAnalysisComponent from '@/components/ImageAnalysisComponent.vue'
export default {
  components: {
    ImageAnalysisComponent
  },
  data: function () {
    return {
      clothes: {
        alias: '',
        image_url: '',
        lower_category: '',
        upper_category: '',
        id: 0,
        owner: '',
        category_id: ''
      },
      analysis_props: {
        upper: '',
        lower: '',
        alias: '',
        category: ''
      },
      categoryData: '',
      noClotheMessage: '',
      noCategoryDataMessage: '',
      disableAnalysis: true,
      alertMessage: '',
      showAlert: false,
      showCategoryAlert: false
    }
  },
  props: [
    'clothes_id',
    'clothes_category',
    'categorydata'
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
      if (vm.clothes_id === undefined) {
        this.$router.push({
          name: 'Bridge',
          params: {
            errorMessage: '해당 옷이 없습니다.',
            destination: 'Closet',
            delay: 3,
            variant: 'danger'
          }
        })
      } else {
        var token = window.localStorage.getItem('token')
        var config = {
          headers: { Authorization: `Bearer ${token}` }
        }
        var clothesId = vm.clothes_id

        axios.get(`${consts.SERVER_BASE_URL}/clothes/${clothesId}/`)
          .then((response) => {
            vm.clothes = response.data
            vm.analysis_props.category = response.data.category_id
            vm.analysis_props.alias = response.data.alias
          }).catch((ex) => {
            this.alertMessage = '해당 옷을 불러올 수 없습니다. 다시 시도해주세요'
            this.showAlert = true
          })

        var categoryId = vm.clothes_category

        axios.get(`${consts.SERVER_BASE_URL}/categorydata/category/?category_id=${categoryId}`, config)
          .then((response) => {
            this.categoryData = response.data
            vm.analysis_props.upper = this.categoryData.upper_category
            vm.analysis_props.lower = this.categoryData.lower_category
            if (this.categoryData.length === 0) {
              this.noCategoryDataMessage = '등록된 옷이 없습니다. 옷을 등록해 주세요'
              this.showCategoryAlert = true
            }
          }).catch((ex) => {
            this.alertMessage = '옷을 불러올 수 없습니다. 다시 시도해주세요'
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
      var clothesId = vm.clothes_id
      var token = window.localStorage.getItem('token')
      var config = {
        headers: { Authorization: `Bearer ${token}` }
      }
      var data = {
        image_url: vm.image,
        alias: vm.analysis_props.alias
      }
      axios.patch(`${consts.SERVER_BASE_URL}/clothes/${clothesId}/`, data, config)
        .then(response => {
          this.alertMessage = '옷의 정보를 수정했습니다.'
          this.showAlert = true
          vm.analysis_props.alias = response.data.alias
          vm.disableAnalysis = true
        }).catch((ex) => {
          this.alertMessage = '해당 옷을 수정할 수 없습니다. 다시 시도해주세요'
          this.showAlert = true
          console.log(ex)
        })
    },
    deleteClothe: function () {
      var vm = this
      var clothesId = vm.clothes_id
      var token = window.localStorage.getItem('token')
      var config = {
        headers: { Authorization: `Bearer ${token}` }
      }
      axios.delete(`${consts.SERVER_BASE_URL}/clothes/${clothesId}/`, config)
        .then(response => {
          this.$router.push({
            name: 'Bridge',
            params: {
              errorMessage: '해당 옷이 삭제되었습니다.',
              destination: 'Closet',
              delay: 3,
              variant: 'success'
            }
          })
        }).catch((ex) => {
          this.alertMessage = '해당 옷을 삭제할 수 없습니다. 다시 시도해주세요'
          this.showAlert = true
          console.log(ex)
        })
    }
  }
}
</script>

<style>

</style>
