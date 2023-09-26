import { Image, TouchableOpacity } from "react-native";
import {Icon} from '../icon/_icon';

import styles from "./_headerBtn.style";

const _headerBtn = ({ icon,handlePress }) => {
  return (
    <TouchableOpacity style={styles.btnContainer} onPress={handlePress}>
       <Icon icon={icon} />
    </TouchableOpacity>
  );
};

export default _headerBtn;