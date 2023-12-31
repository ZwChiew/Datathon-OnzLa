import { createGlobalState } from "react-hooks-global-state";

const { setGlobalState, useGlobalState } = createGlobalState({
  auth: false,
  loading: false,
});

export { useGlobalState, setGlobalState };
