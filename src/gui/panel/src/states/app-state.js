import { reactive, toRefs } from 'vue';

const state = reactive({
    systemSettings: {},
    systemReady: false,
});

function setSystemSettings(value) {
    state.systemSettings = value;
}

function setSystemReady(value) {
    state.systemReady = value;
}

export default function useSharedState() {
    return {
        ...toRefs(state),
        setSystemReady,
        setSystemSettings
    };
}
