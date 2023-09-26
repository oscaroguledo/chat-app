import { Link, Stack } from 'expo-router';
import { Image, Text, SafeAreaView, Button } from 'react-native';
import Header from '../components/header/_header';

function Home() {
    return (
        <SafeAreaView style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Header title="Home"></Header>
            <Text>Home Screen</Text>
        </SafeAreaView>
    );
}

export default Home;