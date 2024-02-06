<script setup>
/* globals pywebview */

import { onMounted } from 'vue';
import useSharedState from './states/app-state';

onMounted(() => {
    window.addEventListener("pywebviewready", () => {
        pywebview.api
            .call("modules.app.initialize")
            .then(() => {
                console.log("PyWebview is ready!");

                pywebview.api
                    .call("modules.system.get_settings")
                    .then((data) => {
                        console.log("System settings is loaded!");

                        const { setSystemReady, setSystemSettings } = useSharedState();

                        setSystemSettings(data);
                        setSystemReady(true);
                    })
                    .catch((e) => {
                        console.log("PyWebview error: " + e);
                    });
            })
            .catch((e) => {
                console.log("PyWebview error: " + e);
            });
    });
});
</script>

<template>
    <router-view />
</template>

<style></style>
