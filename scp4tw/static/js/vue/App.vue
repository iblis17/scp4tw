<template lang="pug">
  section.section
    .container
      .box
        h2.title.is-4.has-text-centered {{ url }}
        p.control.has-addons.has-addons-centered
          input.input(
            placeholder="SCP number"
            v-model="scpNo")
          a.button.is-primary(
            v-on:click="opencc") OpenCC
        p.control.has-addons.has-addons-centered
          a.button(v-bind:href="openccURL")
            span.icon.is-small
              i.fa.fa-link
          a.button(v-bind:href="url")
            span.icon.is-small
              i.fa.fa-external-link
      .box.opencc-box
        p.has-text-centered(v-if="openccURL === ''") 你在想尛？
        object(
          v-if="openccURL !== ''"
          type="text/html"
          v-bind:data="openccURL")
</template>

<script>
import $ from 'jquery'

export default {
  data() {
    return {
      scpNo: '',
      openccURL: '',
    }
  },
  computed: {
    url() {
      const base = 'http://scp-wiki-cn.wikidot.com/scp-'

      if (this.scpNo === '')
        return base

      return `${base}${this.scpNo}`
    },
  },
  methods: {
    opencc() {
      if (this.scpNo === '')
        return

      this.openccURL = `/opencc/${this.scpNo}/`

      const box = $('.opencc-box')
      box.height($('body').height() - $('.box').first().height() - 190)
    },
  },
}
</script>

<style>
html, body, section {
  height: 100%;
}
</style>

<style scoped>
div.columns {
  margin-top: 20px;
}
object {
  width: 100%;
  height: 100%;
}
</style>
