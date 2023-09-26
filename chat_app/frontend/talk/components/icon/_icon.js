import { FontAwesome, FontAwesome5, AntDesign,Feather } from '@expo/vector-icons'; 
import {StyleSheet, Text, View} from 'react-native';
import { COLORS, SIZES } from "../../constants/theme";

function Icon ({icon}){
    return(
        <AntDesign name={icon} size={SIZES.xLarge} color={COLORS.primarytext} style={{"marginHorizontal":SIZES.xSmall}}/>
    );
}
function Icon2({icon}){
    return(
        <Feather name={icon} size={SIZES.xLarge} color={COLORS.primarytext} style={{"marginHorizontal":SIZES.xSmall}}/>
    );
}
export {Icon,Icon2};
