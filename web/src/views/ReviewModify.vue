<template>
  <b-container>
    <b-row cols="1">
      <b-col cols="12">
        <ReviewModifyComponent :review="review"/>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import ReviewModifyComponent from '@/components/ReviewModifyComponent.vue'
export default {
  name: 'reviewmodify',
  components: {
    ReviewModifyComponent
  },
  data: function () {
    return {
    }
  },
  props: [
    'review'
  ]
}
</script>

<style>

</style>
