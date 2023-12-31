import { Link, Stack } from 'expo-router';
import { Image, Text, View, Button, TouchableHighlight, TouchableOpacity  } from 'react-native';
import { COLORS, SIZES } from "../../constants/theme";
import _headerBtn from "../header/_headerBtn";
import {Icon} from '../icon/_icon';
import Profile from '../icon/profile';

const ItemSeparator = () => {
    return (
      <View
       style={{ height: 1, backgroundColor: COLORS.line, marginHorizontal:SIZES.xsmall }}
      />
    );
  };


const Item = ({item, onPress,textColor, rightiteone, rightitetwo}) => (
    <TouchableOpacity onPress={onPress} style={{backgroundColor:COLORS.background, borderRadius:2}}>
        <View style={{flexDirection:'row', alignItems:'center',justifyContent: 'space-between', marginLeft:SIZES.xSmall}}>

          <View style={{flexDirection:'row', alignItems:'center',justifyContent: 'flex-start'}}>
              <Profile iconUrl={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPgNRu3Aj5twxLhAVLEzq5OvIlmvXK8SF4-Q&usqp=CAU"} 
                  dimension={50} size={50} />

              <View  style={{justify:"flex-start",width:150}}>
                  <Text style={{color: textColor,padding:16, paddingBottom:2, fontSize:SIZES.medium, fontWeight:800}}>{item.name}</Text>
                  <Text style={{color: textColor,padding:16,paddingTop:3, fontSize:SIZES.small}}>{item.message}</Text>
              </View>
          </View>

          <View  style={{justify:"flex-start",width:145}}>
              
          </View>
          
          <View style={{width:60}}>
              <Text>
                  {rightiteone}
              </Text>
              <Text>
                  {rightitetwo}
              </Text>
          </View>
        </View>
        
        
    </TouchableOpacity>
  );
const PostItem = ({item, onPress,borderRadius}) => (
    <TouchableOpacity onPress={onPress} style={{backgroundColor:COLORS.background, borderRadius:borderRadius}}>
        <View style={{borderRadius:borderRadius}}>
          <Profile iconUrl={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPgNRu3Aj5twxLhAVLEzq5OvIlmvXK8SF4-Q&usqp=CAU"} 
                  dimension={70} />
        </View>  
    </TouchableOpacity>
  );
const MessageItem = ({item}) => (
  <View style={{minWidth:'30%', maxWidth:'30%',flexDirection:'row', alignItems:'center',justifyContent: 'flex-start'}}>
      <Text>
          {item.name}
      </Text>
  </View>  
);
  

export {
    Item,
    ItemSeparator,
    PostItem,
    MessageItem};
