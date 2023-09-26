import { FontAwesome, FontAwesome5 } from '@expo/vector-icons'; 
import Header from '../components/header/_header';
import {StyleSheet, Text, View, Image, SafeAreaView} from 'react-native';
import { COLORS, SIZES } from "../constants/theme";

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

function Phone ({iconUrl, dimension}){
    return(
      <SafeAreaView>
        <Header title="Groups"></Header>
        <Image
            source={{uri: iconUrl}}
            resizeMode='cover'
            style={styles.btnImg(dimension)}
        />
      </SafeAreaView>
        
    );
}
export default Phone;
