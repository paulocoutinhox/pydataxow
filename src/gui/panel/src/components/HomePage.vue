<script setup>
/* globals pywebview */

import { ref, watch } from 'vue';
import useSharedState from '../states/app-state';
import QrcodeVue from 'qrcode.vue'

const { systemReady, systemSettings } = useSharedState();

const message = ref("");

watch([systemReady], ([value]) => {
    if (value) {
        onSystemIsReady();
    }
}, {
    immediate: true, deep: true
});

function onSystemIsReady() {
    console.log('Panel App Is Ready');
}

function showCurrentTime() {
    pywebview.api
        .call("modules.datetime.get_now", { timestamp: new Date().getTime() })
        .then((result) => {
            message.value = result;
        })
        .catch((e) => {
            message.value = "Error: " + e;
        });
}

function toggleFullscreen() {
    pywebview.api
        .call("modules.system.toggle_fullscreen")
        .then((result) => {
            message.value = result;
        })
        .catch((e) => {
            message.value = "Error: " + e;
        });

    pywebview.api.toggleFullscreen().then((result) => {
        message.value = result;
    });
}

function selectFolder() {
    message.value = "Loading...";

    pywebview.api
        .call("modules.system.select_folder")
        .then((result) => {
            message.value = result;
        })
        .catch((e) => {
            message.value = "Error: " + e;
        });
}

function openURL() {
    message.value = "Loading...";

    pywebview.api
        .call("modules.net.open_url", { url: "https://httpbin.org/get" })
        .then((result) => {
            message.value = result;
        })
        .catch((e) => {
            message.value = "Error: " + e;
        });
}

function playerShow() {
    pywebview.api
        .call("modules.player.show")
        .catch((e) => {
            message.value = "Error: " + e;
        });
}

function playerHide() {
    pywebview.api
        .call("modules.player.hide")
        .catch((e) => {
            message.value = "Error: " + e;
        });
}

function playerUpdateData(data) {
    pywebview.api
        .call("modules.player.update_data", data)
        .catch((e) => {
            message.value = "Error: " + e;
        });
}
</script>

<template>
    <div v-if="systemReady">
        <nav class="navbar is-light is-fixed-top" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <router-link :to="{ name: 'Home' }" class="navbar-item">
                    <img src="../assets/images/logo.png" alt="Logo" style="max-width: 50px" />
                    My App
                </router-link>
            </div>
        </nav>

        <section class="section" style="text-align: center; margin-top: 50px">
            <div class="container">
                <h1 class="title">My App</h1>

                <div class="columns is-mobile is-centered">
                    <div class="column is-full">
                        <img alt="Logo" src="../assets/images/logo.png" style="width: 100px" />
                    </div>
                </div>

                <div class="columns">
                    <div class="column">
                        <button class="button is-primary" @click="playerShow">
                            Player - Show
                        </button>
                    </div>
                    <div class="column">
                        <button class="button is-info" @click="playerHide">
                            Player - Hide
                        </button>
                    </div>
                    <div class="column">
                        <button class="button is-info" @click="playerUpdateData({ type: 'black' })">
                            Player - Update - Clear
                        </button>
                    </div>
                </div>

                <div class="columns">
                    <div class="column">
                        <button class="button is-primary"
                            @click="playerUpdateData({ type: 'image', src: 'https://picsum.photos/1024/768/?blur=2' })">
                            Player - Update - Image
                        </button>
                    </div>
                    <div class="column">
                        <button class="button is-info"
                            @click="playerUpdateData({ type: 'video', src: 'https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4' })">
                            Player - Update - Video
                        </button>
                    </div>
                    <div class="column">
                        <button class="button is-info"
                            @click="playerUpdateData({ type: 'text', text: 'Deus enviou, seu Filho amado, para perdoar, para me salvar' })">
                            Player - Update - Text
                        </button>
                    </div>
                </div>

                <div class="columns">
                    <div class="column">
                        <button class="button is-primary" @click="showCurrentTime">
                            Show current time
                        </button>
                    </div>
                    <div class="column">
                        <button class="button is-info" @click="selectFolder">
                            Select folder
                        </button>
                    </div>
                    <div class="column">
                        <button class="button is-info" @click="toggleFullscreen">
                            Toggle fullscreen
                        </button>
                    </div>
                    <div class="column">
                        <button class="button is-info" @click="openURL">
                            Open URL
                        </button>
                    </div>
                    <div class="column">
                        <router-link :to="{ name: 'About' }">
                            <button class="button is-warning">
                                About
                            </button>
                        </router-link>
                    </div>
                </div>

                <div v-if="message" class="columns is-mobile is-centered" style="margin-top: 30px; margin-bottom: 30px">
                    <div class="column is-full">
                        <article class="message is-info">
                            <div class="message-body">
                                {{ message }}
                            </div>
                        </article>
                    </div>
                </div>

                <qrcode-vue :value="systemSettings.network.rcontrol_url" :size="size" level="H" />
            </div>
        </section>
    </div>
</template>

<style scoped></style>
