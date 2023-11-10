import { useEffect, useState } from 'react';
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
    const [refreshing, setRefreshing] = useState(false);
    const [persons, setPersons] = useState([]);

    const getd_time =(dateString)=>{
      const today = new Date();
      const date = new Date(dateString);
      const daysDifference = (today - date) / (24 * 60 * 60 * 1000);
      let message;

      
      if (daysDifference < 1) {
        // If the difference is less than one day, display the time
        const hours = date.getHours();
        const minutes = date.getMinutes();
        const period = hours < 12 ? "AM" : "PM";
        message = `${hours % 12 || 12}:${minutes.toString().padStart(2, '0')} ${period}`;
      } else if (daysDifference < 30) {
        // If the difference is less than one month, display the number of days ago
        message = `${Math.floor(daysDifference)} day${daysDifference > 1 ? 's' : ''} ago`;
      } else if (daysDifference < 365) {
        // If the difference is less than one year, display the number of months ago
        const monthsDifference = Math.floor(daysDifference / 30);
        message = `${monthsDifference} month${monthsDifference > 1 ? 's' : ''} ago`;
      } else {
        // If the difference is one year or more, display the number of years ago
        const yearsDifference = Math.floor(daysDifference / 365);
        message = `${yearsDifference} year${yearsDifference > 1 ? 's' : ''} ago`;
      }
      return message
    }

    useEffect(() => {
      // Define the API URL you want to fetch data from
      const apiUrl = 'http://127.0.0.1:8000/get_chats_private/101b5318-7793-400b-9755-7a0604796671/'; // Replace with your API endpoint

      fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => {
          // Assuming the API response provides data in the desired format
          console.log(data.chats)
          setPersons(data.chats);
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });
    }, []);
    const onRefresh = () => {
      setRefreshing(true);

      // Refresh data here

      setRefreshing(false);
    };


    const renderItem = ({item}) => {
        const backgroundColor = item.id === selectedId ? COLORS.selectbackground : COLORS.background;
        const color = item.id === selectedId ? COLORS.selectprimaryText : COLORS.primaryText;

        return (
            <View>
                <Item
                    item={item}
                    onPress={() => navigation.dispatch(StackActions.push("UserChat", { id: item.id, name:item.name, messages:item.message }))}
                    backgroundColor={backgroundColor}
                    textColor={color}
                    rightiteone={getd_time(item.dtime)}
                />
                <ItemSeparator/>
            </View>
                    
        );
      };
    return (
        <SafeAreaView style={styles.container}>
            <FlatList
                data={persons}
                refreshing={refreshing}
                onRefresh={onRefresh}
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
    const [refreshing, setRefreshing] = useState(false);

    const onRefresh = () => {
      setRefreshing(true);

      // Refresh data here

      setRefreshing(false);
    };

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
                refreshing={refreshing}
                onRefresh={onRefresh}
                renderItem={renderItem}
                keyExtractor={item => item.id}
                showsVerticalScrollIndicator={false}
                style={{padding:SIZES.xSmall,backgroundColor:COLORS.background}}
            /> 
        </SafeAreaView>
    );
}
  
export {Chats, UserChat};