<template>
  <b-container>
    <b-row cols="1">
      <b-col cols="12">
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios'
import consts from '@/consts.js'
export default {
  name: 'reviewmodify',
  data: function () {
    return {
    }
  },
  props: [
    'clothes_set_id'
  ]
}
</script>

<style>

</style>
