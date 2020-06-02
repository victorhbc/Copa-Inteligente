import * as firebase from 'firebase/app';
import 'firebase/firestore';
import firebaseConfig from '../services/credentials';

class FirebaseInterface {
	constructor() {
		// Initialize firebase connection
		if (!firebase.apps.length) {
			firebase.initializeApp(firebaseConfig);
		}
		this.db = firebase.firestore();
	}
	unsubscribe = () => {};

	changesObserver(document = null, collection, callback) {
		if (document) {
			this.unsubscribe = this.db.collection(collection).doc(document).onSnapshot(function(doc) {
				callback(doc.data());
				console.log(doc.data)
			});
		} else {
			this.unsubscribe = this.db.collection(collection).onSnapshot(function(snapshot) {
				callback(snapshot.docs);
			});
		}
	}

	getData(collection, docName, callback) {
		if (collection && docName) {
			var docRef = this.db.collection(collection).doc(docName);

			docRef
				.get()
				.then(function(doc) {
					if (doc.exists) {
						callback(doc.data());
						
					} else {
						// console.log('No such document!');
					}
				})
				.catch(function(error) {
					// console.log('Error getting document:', error);
				});
		} else {
			callback(null);
		}
	}
}
export default FirebaseInterface;
