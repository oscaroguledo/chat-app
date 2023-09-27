import { useState } from 'react';
import { NavigationContainer, StackActions } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Image, SafeAreaView, FlatList, StyleSheet, Text, View, Button} from 'react-native';
import Header from '../header/_header';
import {ChatItem} from "../chat/_page";
import {Groups} from "../../app/groups"
import {ItemSeparator, Item, MessageItem} from "../List/List_Item";
import { COLORS, SIZES } from '../../constants/theme';


const persons = [
    {
      id: "1",
      name: "Earnest Green",
      messages:[{
        time:"13:00",
        data:"hello wolrd"
      },
      {
        time:"14:00",
        data:"hello wolrd"
      },
      {
        time:"15:00",
        data:"hello wolrd"
      },
      {
        time:"16:00",
        data:"hello wolrd"
      },
      {
        time:"17:00",
        data:"hello wolrd"
      },
      {
        time:"18:00",
        data:"hello wolrd"
      },
      {
        time:"19:00",
        data:"hello wolrd"
      },
      {
        time:"20:00",
        data:"hello wolrd"
      }
    ]
    },
    {
      id: "2",
      name: "Winston Orn",
    },
    {
      id: "3",
      name: "Carlton Collins",
    },
    {
      id: "4",
      name: "Malcolm Labadie",
    },
    {
      id: "5",
      name: "Michelle Dare",
    },
    {
      id: "6",
      name: "Carlton Zieme",
    },
    {
      id: "7",
      name: "Jessie Dickinson",
    },
    {
      id: "8",
      name: "Julian Gulgowski",
    },
    {
      id: "9",
      name: "Ellen Veum",
    },
    {
      id: "10",
      name: "Lorena Rice",
    },
  
    {
      id: "11",
      name: "Carlton Zieme",
    },
    {
        id: "12",
        name: "Jessie Dickinson",
      },
      {
        id: "13",
        name: "Julian Gulgowski",
      },
      {
        id: "14",
        name: "Ellen Veum",
      },
      {
        id: "15",
        name: "Lorena Rice",
      },
      {
        id: "16",
        name: "Jessie Dickinson",
      },
      {
        id: "17",
        name: "Julian Gulgowski",
      },
      {
        id: "18",
        name: "Ellen Veum",
      },
      {
        id: "19",
        name: "Lorena Rice",
      },
    {
      id: "20",
      name: "Jessie Dickinson",
    },
    {
      id: "21",
      name: "Julian Gulgowski",
    },
    {
      id: "22",
      name: "Ellen Veum",
    },
    {
      id: "23",
      name: "Lorena Rice",
    },
  ];

function Chats({ navigation}) {
    const [selectedId, setSelectedId] = useState();

    const renderItem = ({item}) => {
        const backgroundColor = item.id === selectedId ? COLORS.selectbackground : COLORS.background;
        const color = item.id === selectedId ? COLORS.selectprimaryText : COLORS.primaryText;

        return (
            <View>
                <Item
                    item={item}
                    onPress={() => navigation.dispatch(StackActions.push("UserChat", { id: item.id, name:item.name, messages:item.messages }))}
                    backgroundColor={backgroundColor}
                    textColor={color}
                />
                <ItemSeparator/>
            </View>
                    
        );
      };
    return (
        <SafeAreaView style={styles.container}>
            <FlatList
                data={persons}
                renderItem={renderItem}
                keyExtractor={item => item.id}
                extraData={selectedId}
                showsVerticalScrollIndicator={false}
                style={{padding:SIZES.xSmall,backgroundColor:COLORS.background}}
            /> 
        </SafeAreaView>

    );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
    },
    item: {
      padding: 20,
      fontSize: 15,
      marginTop: 5,
    }
  });

function UserChat() {
    const renderItem = ({item}) => {
        return (
            <View>
                <MessageItem
                    item={item}
                />
                <ItemSeparator/>
            </View>
                    
        );
      };

    return (
        <SafeAreaView style={styles.container}>
            <FlatList
                data={persons}
                renderItem={renderItem}
                keyExtractor={item => item.id}
                showsVerticalScrollIndicator={false}
                style={{padding:SIZES.xSmall,backgroundColor:COLORS.background}}
            /> 
        </SafeAreaView>
    );
}
  
export {Chats, UserChat};