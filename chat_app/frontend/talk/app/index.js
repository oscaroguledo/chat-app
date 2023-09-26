import { useState } from 'react';
import { Link, Stack } from 'expo-router';
import { Image, SafeAreaView, FlatList, StyleSheet, Text, View, Button} from 'react-native';
import Header from '../components/header/_header';
import {ItemSeparator, Item} from "../components/List/List_Item";
import { COLORS, SIZES } from '../constants/theme';

const persons = [
    {
      id: "1",
      name: "Earnest Green",
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
function Chats() {
    const [selectedId, setSelectedId] = useState();

    const renderItem = ({item}) => {
        const backgroundColor = item.id === selectedId ? COLORS.selectbackground : COLORS.background;
        const color = item.id === selectedId ? COLORS.selectprimaryText : COLORS.primaryText;
    
        return (
            <View>
                <Item
                    item={item}
                    onPress={() => setSelectedId(item.id)}
                    backgroundColor={backgroundColor}
                    textColor={color}
                />
                <ItemSeparator/>
            </View>
          
        );
      };
    return (
        <SafeAreaView style={styles.container}>
            <Header title="Chats"></Header>
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

export default Chats;

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