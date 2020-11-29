<template>
  <b-container>
    <b-col>
      <b-row no-gutters class="mb-2 form">
        <b-col align-self="center" cols="4">
          <label class="mb-0" for="form-comment">한줄평</label>
        </b-col>
        <b-col cols="8">
          <b-form-input type="text"
                        id="form-comment"
                        v-model="analysis_props.comment"
                        :disabled="isDisabled" />
        </b-col>
      </b-row>
      <b-row no-gutters class="mb-2 form">
        <b-col>
          <b-form-input type="range"
                        id="form-review"
                        v-model="analysis_props.review"
                        min="1" max="5" />
          <b-row>
            <b-col class="col-2 text-left">1</b-col>
            <b-col class="col-3 text-center">2</b-col>
            <b-col class="col-2 text-center">3</b-col>
            <b-col class="col-3 text-center">4</b-col>
            <b-col class="col-2 text-right">5</b-col>
          </b-row>
          <b-row>
            <b-col class="col-4 text-left">추웠다</b-col>
            <b-col class="col-4 text-center">적당했다</b-col>
            <b-col class="col-4 text-right">더웠다</b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-col>
  </b-container>
</template>

<script>
export default {
  props: [
    'analysis_props',
    'isDisabled'
  ]
}
</script>

<style>
.form {
  margin-top: 40px;
}
</style>
