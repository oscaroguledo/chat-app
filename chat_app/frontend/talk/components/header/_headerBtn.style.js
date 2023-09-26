import { StyleSheet } from "react-native";

import { COLORS, SIZES } from "../../constants/theme";

const styles = StyleSheet.create({
  btnContainer: {
    width: 50,
    height: 40,
    backgroundColor: COLORS.background,
    borderRadius: SIZES.small / 1.25,
    justifyContent: "center",
    alignItems: "center",
    marginLeft: "8px",
    marginRight: "8px",
    marginBottom:"0px",
  },
});

export default styles;