import { FontAwesome, FontAwesome5, AntDesign,Feather } from '@expo/vector-icons'; 
import {StyleSheet, Text, View} from 'react-native';
import { COLORS, SIZES } from "../../constants/theme";

function Icon ({icon}){
    return(
        <AntDesign name={icon} size={SIZES.xLarge} color={COLORS.primarytext} />
    );
}
function Icon2({icon}){
    return(
        <Feather name={icon} size={SIZES.xLarge} color={COLORS.primarytext} />
    );
}
export {Icon,Icon2};
