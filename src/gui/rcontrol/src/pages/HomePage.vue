<script setup>
import axios from "axios";
import { ref, watch } from 'vue';
import PageHeader from '../components/PageHeader.vue';
import useSharedState from '../states/app-state';

const { systemReady, apiUrl } = useSharedState();

const playerText = ref("Jesus é bom demais! É isso aí povão! Deus te abençoe!");

watch([systemReady], ([value]) => {
    if (value) {
        onSystemIsReady();
    }
}, {
    immediate: true, deep: true
});

function onSystemIsReady() {
    console.log('Remote Control Is Ready');
}

function playerUpdateData(data, success, error) {
    axios.post(apiUrl.value + '/module/call', {
        func: 'modules.player.update_data',
        params: data,
    })
        .then(() => {
            console.log('OK');

            if (success) {
                success();
            }
        }, (e) => {
            console.log(e);

            if (error) {
                error(e);
            }
        });
}

function playerShow() {
    axios.post(apiUrl.value + '/module/call', { 'func': 'modules.player.show' })
        .then(() => {
            console.log('OK');
        }, (e) => {
            console.log(e);
        });
}

function playerHide() {
    axios.post(apiUrl.value + '/module/call', { 'func': 'modules.player.hide' })
        .then(() => {
            console.log('OK');
        }, (e) => {
            console.log(e);
        });
}

function playerSetText() {
    playerUpdateData({
        'type': 'text',
        'text': playerText.value
    });
}
</script>

<template>
    <div v-if="systemReady">
        <div class="container">
            <PageHeader />

            <div class="row g-3">
                <h3>Player - Text</h3>
                <div class="mb-3">
                    <label for="inputNewText" class="form-label">New Text</label>
                    <input :value="playerText" type="email" class="form-control" id="inputNewText">
                </div>
                <button type="button" class="btn btn-primary" @click="playerSetText">Send</button>
            </div>

            <hr>

            <div class="row g-3">
                <h3>Player - Control</h3>
                <div class="col-auto">
                    <button type="button" class="btn btn-primary" @click="playerShow">Show Player</button>
                </div>
                <div class="col-auto">
                    <button type="button" class="btn btn-primary" @click="playerHide">Hide Player</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
