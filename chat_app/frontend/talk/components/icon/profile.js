import { FontAwesome, FontAwesome5 } from '@expo/vector-icons'; 
import {StyleSheet, Text, View, Image} from 'react-native';
import { COLORS, SIZES } from "../../constants/theme";

const styles = StyleSheet.create({
    btnContainer: {
      width: 40,
      height: 40,
      backgroundColor: COLORS.white,
      borderRadius: SIZES.small / 1.25,
      justifyContent: "center",
      alignItems: "center",
    },
    btnImg: (dimension) => ({
      width: dimension,
      height: dimension,
      borderRadius: SIZES.small / 1.25,
    }),
  });

function Profile ({iconUrl, dimension}){
    return(
        <Image
            source={{uri: iconUrl}}
            resizeMode='cover'
            style={styles.btnImg(dimension)}
        />
    );
}
export default Profile;
